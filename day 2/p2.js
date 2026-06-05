// let content = document.querySelector("div")
// console.log(content)

// function changeColor(){
// if(content.style.backgroundColor === "white"){
//     content.style.backgroundColor="rgb(41, 139, 171)"
// }else{
//     content.style.backgroundColor="white"
// }}


let theCircle=document.getElementById("circle")
console.log(theCircle)

function changeColor(){
    if(theCircle.style.backgroundColor === "white"){
        theCircle.style.backgroundColor="red"
    }else if(theCircle.style.backgroundColor === "red"){
        theCircle.style.backgroundColor="yellow"
    }else if(theCircle.style.backgroundColor === "yellow"){
        theCircle.style.backgroundColor="green"
    }else if(theCircle.style.backgroundColor === "green"){
        theCircle.style.backgroundColor="blue"
    }else if(theCircle.style.backgroundColor === "blue"){
        theCircle.style.backgroundColor="purple"
    }else if(theCircle.style.backgroundColor === "purple"){
        theCircle.style.backgroundColor="pink"
    }else if(theCircle.style.backgroundColor === "pink"){
        theCircle.style.backgroundColor="orange"
    }else if(theCircle.style.backgroundColor === "orange"){
        theCircle.style.backgroundColor="black"
    }
    else{
        theCircle.style.backgroundColor="white"
    }
}