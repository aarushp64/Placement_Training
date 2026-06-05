let content = document.querySelector("h1")
console.log(content)
let btn = document.querySelector("button")
console.log(btn)
btn.addEventListener("click", ()=>{
if(content.textContent === "Hello, World!"){
    content.textContent="i am learning advanced js"
}else{
    content.textContent="Hello, World!"
}})

// btn.addEventListener("click", ()=>{
//     content.textContent="i am learning advanced js"
//     content.style.color="lightblue"
// })

