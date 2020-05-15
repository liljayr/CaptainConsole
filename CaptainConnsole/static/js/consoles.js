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
});

function update_favorites() {
    $('#console :checked').each(function(index){
    });
};

//values in quotes are id in template
function performSearch(){
    let query = $('#search-box').val();
    let sort = $('#sort-by').val();
    let count = 0;
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