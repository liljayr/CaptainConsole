function insertLocalStorage(button) {

        button.onclick = function () {
            let product_id = 0;
            $('#game :button').each(function(index){
                product_id = this.value;
                console.log(product_id);
            });
                    localStorage.setItem("id", product_id );

            }

};

let button = document.getElementById("view");
insertLocalStorage(button);

