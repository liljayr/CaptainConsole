// create json string for cart "[{\"country\":\"Iceland\"}]"

function addCartToStorage() {
    //búa til cart item í localStorage og setja inní það
    let dict = {
        product_id: 4,
        type: "console",
        amount: 1
    }
    let array = []
    array.push(dict)
    let cart_item = JSON.stringify(array)
    localStorage.setItem("cart",cart_item)
}

function addToCart() {
    let add_to_cart_button = document.getElementById("{{ games.id }}")
    add_to_cart_button.onclick = function () {
        let product_id = 
        let current_cart = localStorage.getItem("cart")
        //Bæta við tölu hjá cart
        if (current_cart === null) {
            let cart_counter = 1;
            addCartToStorage()
        }
        else {
            cart_counter += 1;

            let dict2 = {
                product_id: 4,
                type: "console",
                amount: 1
            }
            let cart_items = JSON.parse(localStorage.getItem("cart"))
            let item_exists = false;
            for (let i = 0; i < cart_items.length; i++) {
                console.log(dict2.product_id == cart_items[i].product_id)
                if (dict2.product_id == cart_items[i].product_id) {
                    cart_items[i].amount += 1;
                    item_exists = true
                }
            }
            if (item_exists == false) {
                cart_items.push(dict2)

                let str_cart_item = JSON.stringify(cart_items)
                localStorage.setItem("cart", str_cart_item)
                //ath hvort type (game/console) og id er til í cart þá hækka amount um 1
                //annars bæta við nýju product í cart
            }
        }
        document.getElementById("cart_img").innerHTML = cart_counter;

        location.reload();
        };
};

addToCart()

