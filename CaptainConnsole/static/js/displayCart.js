function displayInCart() {
        let cart_str = localStorage.getItem("cart");
        if (cart_str != null) {
            let cart = JSON.parse(cart_str);
            let cart_div = document.getElementById("cart_div");
            let cart_items = document.getElementById("cart_items");
            let total_price = 0;

            for (let i=0; i<cart.length;i++) {
                let product_info = cart[i].product_id.split("_");
                let type = product_info[0];
                let id = product_info[1];
                let name = product_info[2];
                let price = JSON.parse(product_info[3]);
                let amount = JSON.parse(cart[i].amount);

                total_price += price * amount;

                cart_items.innerHTML += `<div class="cart_single_item">
                                                <p>` + name + `</p>
                                                <p>` + amount + `</p>
                                                <p>$` + price + `</p>
                                            </div>`
                if (i == (cart.length)-1) {
                    cart_div.innerHTML += `<div class="total_price">
                                                <p>Total price: $` + total_price + `</p>
                                          </div>`

                };
            }
        }



};


let button = document.getElementById("cart_img");
button.onclick = function() {
    $(document).ready(displayInCart());
}
