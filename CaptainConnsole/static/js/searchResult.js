
function getSearchResults(product_type) {
    $('#search-btn').on('click',function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/'+product_type + '?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class='well ' + product_type">
                                <a href= '/' + product_type + '/${d.id}">
                                    <img class="game_img" src="${d.firstImage}" />
                                    <p>${d.name}</p>
                                    <p>${d.price}</p>
                                </
                                a>
                            </div>`
                });
                $('.'+product_type).html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                // TODO: Show toastr
                console.error(error);
            }
        })
    });
};

$(document).ready(getSearchResults("games"))
$(document).ready(getSearchResults("consoles"))

