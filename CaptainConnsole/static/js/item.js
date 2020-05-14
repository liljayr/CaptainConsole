$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        performSearch();
    });
    $('.item').click(function() {
        performSearch();
    });
    $('.star').click(function() {
        update_favorites();
    });
    $('.sortbtn').click(function() {
        console.log("checking stuff");
        console.log($(this));
        console.log($(this)[0].id);
        let btnvalue=$(this)[0].id;
        performSearch(btnvalue);
    })
});

function update_favorites() {
    $('#game :checked').each(function(index){
        console.log($(this));
        console.log(this.value);
    });
};

//values in quotes are id in template
function performSearch(sort_btn){
    let query = $('#search-box').val();
    let getConsoles = new Array();
    let type = new Array();
    let hiddenValue = $('#hidden')[0].innerText;
    let count = 0;
    let count2 = 0;
    let on_sale = 'False';
    $('#consoleCatG :checked').each(function(index) {
        //console.log("Sorting games!!!!");
        //consoles = consoles
        //console.log($(this));
        //console.log(this.value);
        getConsoles[count] = this.value;
        count = count + 1;
    });
    $('#types :checked').each(function(index) {
        type[count2] = this.value;
        count2 = count + 1;
    })
    $('.on-sale :checked').each(function(index) {
        on_sale = 'True';
    })
    //console.log(consoles);
    let types = '';
    let comp_url = '/' + hiddenValue + '?search_filter=' + query + '&check=' + getConsoles + '&type=' + type +
        '&sort_by=' + sort_btn + '&on_sale=' + on_sale;
    console.log("url check");
    console.log(comp_url);
    $.ajax({
        url: comp_url,
        type: 'GET',
        success: function(resp){
            let newHtml = resp.data.map(d => {
                return `<div class="well-item">
                            <a href="/${hiddenValue}/${d.id}">
                                <img class="item-img" src="${d.first_image}"/>
                                <h4>${d.name}</h4>
                                <h4>$${d.price}</h4>
                            </a>
                        </div> `
            });
            $('.items').html(newHtml.join(''));
            $('#search-box').val('');
        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            console.error(error);
        }
    });
};