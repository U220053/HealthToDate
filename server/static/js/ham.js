console.log("S");
hamburger = document.getElementById('menu')
change = document.getElementById('chng')


hamburger.addEventListener('click', ()=>{
    change.classList.toggle("chng");
})