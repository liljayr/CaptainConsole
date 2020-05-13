/*$(document).ready(function(){
    $('#search-btn').on( 'click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/games?search_filter=' + searchText,
            type: 'GET',
            success: function(resp){
                var newHtml = resp.data.map(d => {
                    return `<div class="well-game">
                                <a href="/games/${d.id}">
                                    <img class="game-img" src="${d.first_image}"/>
                                    <h4>${d.name}</h4>
                                    <h4>$${d.price}</h4>
                                </a>
                            </div> `
                });
                $('.games').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                // TODO: Show toastr
                console.error(error);
            }
        });
    });
});*/

$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        performSearch();
    });
    console.log("console check");
    console.log($('#consoles'));
    $('#consoles').on('click', function(e) {
        performSearch();
    })
});

//values in quotes are id in template
function performSearch(){
    var query = $('#search-box').val();
    var sort = $('#sort-by').val();
    var consoles = new Array();
    var count = 0;
    $('#consoles :checked').each(function(index) {
        //consoles = consoles
        console.log($(this));
        console.log(this.value);
        consoles[count] = this.value;
        count = count + 1;
    });
    console.log(consoles);
    var types = '';
    var comp_url = '/games?search_filter=' + query + '&check=' + consoles; //+ '&sort_by=' + sort
    $.ajax({
        url: comp_url,
        type: 'GET',
        success: function(resp){
            var newHtml = resp.data.map(d => {
                return `<div class="well-game">
                            <a href="/games/${d.id}">
                                <img class="game-img" src="${d.first_image}"/>
                                <h4>${d.name}</h4>
                                <h4>$${d.price}</h4>
                            </a>
                        </div> `
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