$(document).ready(function(){
    console.log("HEYYYY");
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        console.log("Searching");
        performSearch();
    });
    console.log("console check");
    console.log($('#consoles'));
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
    $('#console :checked').each(function(index){
        console.log($(this));
        console.log(this.value);
    });
};

//values in quotes are id in template
function performSearch(){
    let query = $('#search-box').val();
    let sort = $('#sort-by').val();
    console.log("checking query");
    console.log(query);
    //let consoles = new Array();
    let count = 0;
    /*$('#consoles :checked').each(function(index) {
        //consoles = consoles
        console.log($(this));
        console.log(this.value);
        consoles[count] = this.value;
        count = count + 1;
    });*/
    //console.log(consoles);
    let types = '';
    let comp_url = '/consoles?search_filter=' + query;// + '&check=' + consoles; //+ '&sort_by=' + sort
    $.ajax({
        url: comp_url,
        type: 'GET',
        success: function(resp){
            let newHtml = resp.data.map(d => {
                return `<div class="well-item">
                            <a href="/consoles/${d.id}">
                                <img class="item-img" src="${d.first_image}"/>
                                <h4>${d.name}</h4>
                                <h4>$${d.price}</h4>
                            </a>
                        </div>`
            });
            $('.games').html(newHtml.join(''));
            $('#search-box').val('');
        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            console.error(error);
        }
    });
};