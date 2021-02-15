let email = document.querySelector("#email");
let pw = document.querySelector("#pass");
let loginBtn = document.querySelector(".submitbtn");
let registerbtn = document.querySelector(".registerbtn");
let message = document.querySelector(".message");
let burgerNavBar = document.querySelector(".burger-nav");
let navBarSlide = document.querySelector(".nav-btn-slide")

window.addEventListener("load" , function(){
    burgerNavBar.addEventListener("click", burgerNav);
    loginBtn.addEventListener("click" , submitbtnHandler);
    registerbtn.addEventListener("click", registerbtnHandler);
})

function registerbtnHandler(){
    window.location.href = "/signup"
}

function burgerNav(){
    if( navBarSlide.classList.contains("active")){
        navBarSlide.classList.remove("active");
    }else{
        navBarSlide.classList.add("active");
    }
    
}


async function submitbtnHandler(e){
    try{
        e.preventDefault(); // prevent page refresh
        if(email.value && pw.value){
            console.log(email.value, pw.value);
            let obj = await axios.post( "https://foodcolony.herokuapp.com/user/login" , {email:email.value , password:pw.value});

            
            console.log(obj);
            if(obj.data.data){
                window.location.href = "/menu";
            }else{
                message.innerHTML = obj.data.message;
            }
        }
    }
    catch(error){
        console.log(error);
    }
}