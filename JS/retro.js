
let degx=1

let degy=1

let x=397.2

let y=250

let hell=document.getElementById("hell")

let rightborder= document.getElementById("rightborder1")

let leftborder= document.getElementById("leftborder1")

let a = document.getElementById("texthey")

let khat = document.getElementById("khat1")

function collidesWith (element1, element2) {

    var Element1 = {};

    var Element2 = {};


    
    Element1.top = $(element1).offset().top;
    
    Element1.left = $(element1).offset().left;
    
    Element1.right = Number($(element1).offset().left) + Number($(element1).width());
    
    Element1.bottom = Number($(element1).offset().top) + Number($(element1).height());


    
    Element2.top = $(element2).offset().top;
    
    Element2.left = $(element2).offset().left;
    
    Element2.right = Number($(element2).offset().left) + Number($(element2).width());
    
    Element2.bottom = Number($(element2).offset().top) + Number($(element2).height());


    
    if (Element1.right > Element2.left && Element1.left < Element2.right && Element1.top < Element2.bottom && Element1.bottom > Element2.top) {
    
        return true
    
    }
    
    else{
    
        return false
    
    }
}


function moving(){

    a.setAttribute('cx', x);

    a.setAttribute('cy', y);

    if(collidesWith ( a, rightborder ) || collidesWith ( a, leftborder )){

        degx=-degx

    }

    if(!collidesWith ( a, hell )){

        degy=-degy

    }

    x+=1*degx

    y+=1*degy

    
    
    setTimeout('moving()',0.1)


}




moving()



let leftbr = document.getElementById("leftborder")



let rightbr = document.getElementById("rightborder")



let lastb = leftbr.style.top



let lastr = rightbr.style.top



let leftbr1 = document.getElementById("leftborder1")



let rightbr1 = document.getElementById("rightborder1")



let lastb1 = leftbr.style.top



let lastr1 = rightbr.style.top



document.addEventListener('keypress',function(e){


    
    if(e.key == 's'){


        
        if(lastb == 400){Number(lastb) = 400}
        
        lastb = Number(lastb) + 10
        
        leftbr.style.top = `${lastb}px` 


        
        if(lastb1 == 400){Number(lastb1) = 400}
        
        lastb1 = Number(lastb1) + 10
        
        leftbr1.style.top = `${lastb1}px` 
    }

    
    else if(e.key == 'w'){


        
        if(lastb == 0){Number(lastb) = 0}
        
        lastb = Number(lastb) - 10
        
        leftbr.style.top = `${lastb}px` 


        
        if(lastb1 == 0){Number(lastb1) = 0}
        
        lastb1 = Number(lastb1) - 10
        
        leftbr1.style.top = `${lastb1}px` 
    }

    
    else if(e.key == 'l'){


        
        if(lastr == 400){Number(lastr) = 400}
        
        lastr = Number(lastr) + 10
        
        rightbr.style.top = `${lastr}px`


        
        if(lastr1 == 400){Number(lastr1) = 400}
        
        lastr1 = Number(lastr1) + 10
        
        rightbr1.style.top = `${lastr1}px`
    }

    
    else if(e.key == 'o'){


        
        if(lastr1 == 0){Number(lastr1) = 0}
        
        lastr1 = Number(lastr1) - 10
        
        rightbr1.style.top = `${lastr1}px`


        
        if(lastr == 0){Number(lastr) = 0}
        
        lastr = Number(lastr) - 10
        
        rightbr.style.top = `${lastr}px`
    }



});
/*document.addEventListener('mousemove' , (e)=> {
    console.log(e.clientX,e.clientY)
})*/