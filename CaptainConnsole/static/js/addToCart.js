

function addCartToStorage(dict) {
    //búa til cart item í localStorage og setja inní það
    let array = [];
    array.push(dict);
    let cart_item = JSON.stringify(array);
    localStorage.setItem("cart",cart_item);
};


function getCartCounter() {
    let cart = JSON.parse(localStorage.getItem("cart"));
    let cart_counter = 0;
    for (let i=0; i<cart.length; i++) {
        cart_counter += cart[i].amount;
    }

    document.getElementById("num_in_cart").innerHTML = cart_counter;
}

function enoughInStock() {
    let amount_in_stock = document.getElementById("amount_in_stock");
    if (amount_in_stock > 0) {
        return true;
    };
    return false;
};



function addToCart() {
    let add_to_cart = document.getElementById("add_button_games");
    add_to_cart.onclick = function () {
        let product_id = -1;
        $('#add_button_div :button').each(function(index){
            product_id = this.value;
        });
        let current_cart = localStorage.getItem("cart");
        if (current_cart === null) {
            let dict = {
                product_id: product_id,
                amount: 1
                };
                addCartToStorage(dict);
        }
        else {
            let cart_items = JSON.parse(localStorage.getItem("cart"));
            let item_exists = false;
            for (let j = 0; j < cart_items.length; j++) {
                if (product_id == cart_items[j].product_id) {
                    cart_items[j].amount += 1;
                    item_exists = true;
                };
            }
            if (item_exists == false) {
                let dict = {
                    product_id: product_id,
                    amount: 1
                };
                cart_items.push(dict);
            }
            let str_cart_item = JSON.stringify(cart_items);
            localStorage.setItem("cart", str_cart_item);
        }
        getCartCounter();
    };

};

let add_to_cart = document.getElementById("add_button_games");
add_to_cart.onclick = function() {
    $(document).ready(addToCart());
}


function addToDB() {
    console.log("DB FUNC");
};

$(document).ready(addToCart());






