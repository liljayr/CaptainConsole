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
                let total_price2 = total_price.toFixed(2);

                cart_items.innerHTML += `<div class="cart_single_item">
                                                <div class="item_info">` + name + `</div>
                                                <div class="item_info">` + amount + `</div>
                                                <div class="item_info">$` + price + `</div>
                                            </div>`
                if (i == (cart.length)-1) {
                    cart_div.innerHTML += `<div class="total_price">
                                                <p class="total_price_cart">Total price: $` + total_price2 + `</p>
                                          </div>`

                };
            }
        }



};


let button = document.getElementById("cart_img");
button.onclick = function() {
    $(document).ready(displayInCart());
}
