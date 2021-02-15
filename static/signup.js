let username = document.querySelector("#name");
let email = document.querySelector("#email");
let cusername = document.querySelector(".cname .value");
let cemail = document.querySelector(".cemail .value");
let pw = document.querySelector("#pw");
let cpw = document.querySelector("#cpw");
let phone = document.querySelector("#phone");
let cphone = document.querySelector(".cph .value");
let org = document.querySelector("#orgName");
let corg = document.querySelector(".corg .value ");
let eid = document.querySelector("#eid");
let ceid = document.querySelector(".ceid .value");
let id = document.querySelector("#eidImg");
let cid = document.querySelector(".ceidpic img");
let signupBtn = document.querySelector(".submitbtn");
let mess = document.querySelector(".message")
let burgerNavBar = document.querySelector(".burger-nav");
let navBarSlide = document.querySelector(".nav-btn-slide")
let cpage = document.querySelector(".confirmpage")
let cbtn = document.querySelector(".confirm");
let editbtn = document.querySelector(".edit");
let loginbtn = document.querySelector(".loginbtn");

window.addEventListener("load", function () {
    burgerNavBar.addEventListener("click", burgerNav)
    loginbtn.addEventListener("click",loginbtnHandler);
    signupBtn.addEventListener("click", signupBtnHandler);
    cbtn.addEventListener("click",cbtnHandler);
    editbtn.addEventListener("click", editbtnHandler);
})
function loginbtnHandler(){
    window.location.href = "/login";
}
function burgerNav() {
    if (navBarSlide.classList.contains("active")) {
        navBarSlide.classList.remove("active");
    } else {
        navBarSlide.classList.add("active");
    }

}

function signupBtnHandler (e) {
    e.preventDefault();
    
    if (username.value && email.value && pw.value && cpw.value && id.files[0]) {
        mess.innerHTML = "";
        cusername.innerHTML = username.value;
        cemail.innerHTML = email.value;
        cphone.innerHTML = phone.value;
        corg.innerHTML = org.value;
        ceid.innerHTML = eid.value;
        let reader = new FileReader();
        reader.onload = function (e) {
            // cid.src = e.target.result;
            cid.setAttribute("src", e.target.result);
        };
        reader.readAsDataURL(id.files[0]);

        cpage.classList.add("block");
    }else{
        mess.innerHTML = "All fields are mandatory!!";
    }
}
async function cbtnHandler (e) {
    try {
        e.preventDefault(); // prevent page refresh
        let formData = new FormData();
        let file = id.files[0];
        formData.append("eidpic" , file);
        formData.append("username" , username.value);
        formData.append("email" , email.value);
        formData.append("phone" , phone.value);
        formData.append("org" , org.value);
        formData.append("eid" , eid.value);
        formData.append("password" , pw.value);
        formData.append("confirmPassword" , cpw.value);
        let obj = await axios.post("https://foodcolony.herokuapp.com/user/signup", formData);
        
        console.log(obj);
        if (obj.data.data) {
            window.location.href = "/menu";
        } else {
            mess.innerHTML = obj.data.message;
        }
    }
    catch (error) {
        
        cpage.classList.remove("block");
        mess.innerHTML = "INVALID DETAILS";
        console.log(error);
    }
}

function editbtnHandler () {
    cpage.classList.remove("block");
}