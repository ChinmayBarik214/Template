const item2 = document.querySelector(".four-item2");
const item3 = document.querySelector(".four-item3");
const position2=item2.getBoundingClientRect().top;
const position3=item3.getBoundingClientRect().top;
const screenPosition=window.innerHeight;

window.addEventListener('scroll',()=>{
    const item2 = document.querySelector(".four-item2");
    const position2=item2.getBoundingClientRect().top;
    const screenPosition=window.innerHeight;

    if(screenPosition>(position2+50)){
        item2.classList.add('active');
    }else{
        item2.classList.remove('active');
    }
})
window.addEventListener('scroll',()=>{
    const item3=document.querySelector(".four-item3");
    const position3=item3.getBoundingClientRect().top;
    const screenPosition=window.innerHeight;
    if(screenPosition>(position3+50)){
        item3.classList.add('active');
    }else{
        item3.classList.remove('active')
    }
})
