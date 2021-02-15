let burgerNavBar = document.querySelector(".burger-nav");
let navBarSlide = document.querySelector(".nav-btn-slide")

window.addEventListener("load" , function(){
    burgerNavBar.addEventListener("click", burgerNav)
})

function burgerNav(){
    if( navBarSlide.classList.contains("active")){
        navBarSlide.classList.remove("active");
    }else{
        navBarSlide.classList.add("active");
    }
    
}
