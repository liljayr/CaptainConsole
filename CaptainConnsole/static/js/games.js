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
    /*$('#checkbox').on('click', function(e) {
        performSearch();
    })*/
});

function update_favorites() {
    $('#game :checked').each(function(index){
        console.log($(this));
        console.log(this.value);
    });
};

//values in quotes are id in template
function performSearch(){
    let query = $('#search-box').val();
    let sort = $('#sort-by').val();
    let getConsoles = new Array();
    let count = 0;
    $('#consoleCatG :checked').each(function(index) {
        console.log("Sorting games!!!!");
        //consoles = consoles
        console.log($(this));
        console.log(this.value);
        getConsoles[count] = this.value;
        count = count + 1;
    });
    //console.log(consoles);
    let types = '';
    let comp_url = '/games?search_filter=' + query + '&check=' + getConsoles; //+ '&sort_by=' + sort
    console.log("url check");
    console.log(comp_url);
    $.ajax({
        url: comp_url,
        type: 'GET',
        success: function(resp){
            let newHtml = resp.data.map(d => {
                return `<div class="well-item">
                            <a href="/games/${d.id}">
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