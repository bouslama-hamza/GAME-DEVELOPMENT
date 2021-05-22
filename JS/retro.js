let leftbr = document.getElementById("leftborder")

let rightbr = document.getElementById("rightborder")

let text = document.getElementById("text")

let lastb = leftbr.style.top

let lastr = rightbr.style.top

document.addEventListener('keypress',function(e){

    if(e.key == 's'){

        if(lastb == 400){Number(lastb) = 400}
        lastb = Number(lastb) + 10
        leftbr.style.top = `${lastb}px` 

    }
    else if(e.key == 'w'){

        if(lastb == 0){Number(lastb) = 0}
        lastb = Number(lastb) - 10
        leftbr.style.top = `${lastb}px` 

    }
    else if(e.key == 'l'){

        if(lastr == 400){Number(lastr) = 400}
        lastr = Number(lastr) + 10
        rightbr.style.top = `${lastr}px`

    }
    else if(e.key == 'o'){

        if(lastr == 0){Number(lastr) = 0}
        lastr = Number(lastr) - 10
        rightbr.style.top = `${lastr}px`
        
    }

});



