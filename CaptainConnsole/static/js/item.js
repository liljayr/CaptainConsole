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
    let favorite_list = [];
    let game_id = -1;
    $('#game :checked').each(function(index){
        game_id = this.value;
        favorite_list.push(game_id);
        console.log(favorite_list);
        console.log(this.value);

    });
    let hiddenValue = $('#hidden')[0].innerText;
    console.log(hiddenValue);
    let user_id = $('#hidden_view')[0].innerText;
    console.log(user_id);
    let fav_url = 'addfavorites';
        $.ajax({
            url: fav_url,
            data: {'favorite_item': game_id, 'user_id':user_id},
            type: 'POST'
    }).done(function (response) {
        console.log(response);

        })



};

//values in quotes are id in template
function performSearch(sort_btn){
    let query = $('#search-box').val();
    //let sort = $('.sortbtn');
    console.log("sort");
    console.log(sort_btn);
    let getConsoles = new Array();
    let hiddenValue = $('#hidden')[0].innerText;
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
    let comp_url = '/' + hiddenValue + '?search_filter=' + query + '&check=' + getConsoles+ '&sort_by=' + sort_btn; //+ '&type=' + type
    console.log("url check");
    console.log(comp_url);
    $.ajax({
        url: comp_url,
        type: 'GET',
        csrfmiddlewaretoken: '{{ csrf_token }}',
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