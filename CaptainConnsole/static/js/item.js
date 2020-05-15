$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        performSearch();
    });
    $('.item').click(function() {
        performSearch();
    });
    $('.star').click(function() {
        performSearch();
    });
    $('.sortbtn').click(function() {
        let btnvalue=$(this)[0].id;
        performSearch(sort_btn=btnvalue);
    })
});

function update_favorites() {
    let favorite_list = [];
    let prod_id = -1;
    $('#games :checked').each(function(index){
        prod_id = this.value;
        favorite_list.push(prod_id);
    });
    $('#consoles :checked').each(function(index){
        prod_id = this.value;
        favorite_list.push(prod_id);
    });
    return prod_id;
};

//values in quotes are id in template
function performSearch(sort_btn ){
    let query = $('#search-box').val();
    let getConsoles = new Array();
    let type = new Array();
    let hiddenValue = $('#hidden')[0].innerText;
    let count = 0;
    let count2 = 0;
    let on_sale = 'False';
    let prod_id = update_favorites();
    $('#consoleCatG :checked').each(function(index) {
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
    let types = '';
    let comp_url = '/' + hiddenValue + '?search_filter=' + query + '&check=' + getConsoles + '&type=' + type +
        '&sort_by=' + sort_btn + '&on_sale=' + on_sale + '&hidden=' + hiddenValue +  '&prod_id=' + prod_id;
    console.log("url check");
    console.log(comp_url);
    $.ajax({
        url: comp_url,
        type: 'GET',
        csrfmiddlewaretoken: '{{ csrf_token }}',
        success: function(resp){
            let newHtml = resp.data.map(d => {
                return `<link rel="stylesheet" href="{%static 'css/item.css' %}"/>
                        <p class="hide" id="hidden_view" name="view" >{{ current_user_id }}</p>
                        <div class="well-item" id="${hiddenValue}">
                            <form action="/${hiddenValue}/${d.id}" >
                                <button class="view " id="view_${d.id}"  type="submit" value="${hiddenValue}_${d.id}">
                                    <img class="item-img" src="${d.first_image}" alt="No picture available"/>
                                    <h4>${d.name}</h4>
                                    <h4>$${d.price}</h4>
                                    <input type="checkbox" value="${d.id}" class="star" name="star">
                                </button>
                            </form>
                        </div> `
            });
            $('.items').html(newHtml.join(''));
        },
        error: function (xhr, status, error) {
            // TODO: Show toastr
            console.error(error);
        }
    });
};