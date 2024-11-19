let url = 'https://script.google.com/macros/s/AKfycbyA7oUnDuFd-5wJB-MbT4qx2nC3qXwNuSpVa_x9cgWF4edyqT3bMdFglmNTYOzd8-iG/exec'
    let form = document.querySelector('#form');
    form.addEventListener("submit", (e) =>{
        e.target.btn.innerHTML = "Submitting...";
        let d = new FormData(form)
        fetch(url,{
            method:"POST",
            body:d
        }).then((res) => res.text())
        .then((finalRes) =>{
            e.target.btn.innerHTML = "Submitted";
            console.log(finalRes)
            form.reset();

        })
        e.preventDefault();
    })