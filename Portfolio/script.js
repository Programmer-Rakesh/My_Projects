const sideMenu = document.querySelector('#sideMenu');
const navBar = document.querySelector("nav");
const navLinks = document.querySelector("nav ul");

function openMenu(){
    sideMenu.style.transform = 'translateX(-16rem)';
}
function closeMenu(){
    sideMenu.style.transform = 'translate(16rem)';
}

window.addEventListener('scroll', ()=>{
    if(scrollY > 50){
        navBar.classList.add('bg-white', 'bg-opacity-50', 'backdrop-blur-lg'
            , 'shadow-sm'
        );
        navLinks.classList.remove('bg-white', 'shadow-sm', 'bg-opacity-50')
    }
    else{
        navBar.classList.remove('bg-white', 'bg-opacity-50', 'backdrop-blur-lg'
            , 'shadow-sm'
        );
        navLinks.classList.add('bg-white', 'shadow-sm', 'bg-opacity-50')
    }
})
//--------- light mode / dark mode

// document.documentElement.classList.toggle(
//   'dark',
//   localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)
// )

