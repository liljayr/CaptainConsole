

function hideImg(){
    let g_name = document.getElementById("g_name");
    let game = document.getElementById("game");
    let console = document.getElementById("console")
    if(g_name){
        game.classList.remove("hide");
        console.classList.add("hide")
    }else{
        console.classList.remove("hide");
        game.classList.add("hide")
    }


};



hideImg()




