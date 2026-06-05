let photo = document.querySelector("img")
console.log(photo)
let btn1 = document.querySelectorAll("button")[0]
console.log(btn1)

btn1.addEventListener("click", ()=>{
    photo.src="happy.jpg"
})
let btn2 = document.querySelectorAll("button")[1]
console.log(btn2)

btn2.addEventListener("click", ()=>{
    photo.src="sad.png"
})