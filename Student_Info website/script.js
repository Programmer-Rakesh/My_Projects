function search() {
        let okay = document.getElementById("a").value;
        let f = document.getElementById("f");
        let pp = document.getElementById("um")
        let ww = document.getElementById("op")
        let vg = document.getElementById("ou")
        let vp = document.getElementById("ot")
        let vs = document.getElementById("os")

        let img = document.createElement("img");
        img.width = 160;
        

            if ( okay==="24SECE1030051" ||  okay==="51"  || okay==="Rakesh Roy" || okay==="rakesh"  || okay==="Rakesh"){
                f.value = "Rakesh Roy";
                img.src = "./images/pp.jpg"
                ww.value = "Roll no : 24SECE130051"
                vg.value = "Date of Joining : 19/08/2024"
                vp.value = "Course : BTech ECE"
                vs.value = "Specialisation : AI & ML"
            }
            else if ( okay==="24SECE1030020" ||  okay==="20"  || okay==="Piyush kumar singh" || okay === "Piyush"  || okay==="Piyush kumar" || okay ==="piyush"){
                f.value = "Piyush Kumar Singh";
                img.src = "./images/pp2.jpg"
                ww.value = "Roll no : 24SECE130020"
                vg.value = "Date of Joining : 25/08/2024"
                vp.value = "Course : BTech CSE"
                vs.value = "Specialisation : AI"
            }
            else if ( okay==="24SECE1030012" ||  okay==="12"  || okay==="Subrat Upadhyay" || okay === "Subrat"  || okay==="Piyush upadhyay" || okay ==="subrat upadhyay"  || okay==="subrat"){
                f.value = "Subrat Upadhyay";
                img.src = "./images/pp3.jpg"
                ww.value = "Roll no : 24SECE130012"
                vg.value = "Date of Joining : 22/08/2024"
                vp.value = "Course : BTech CSE"
                vs.value = "Specialisation : Data Science"
            }
            else{
                f.value = "Eren Eager";
                img.src ="./images/else.jpg"
                ww.value = "Roll no : 24SECE130051"
                vg.value = "Date of Joining : 25/08/2024"
                vp.value = "Course : BTech CSE"
                vs.value = "Specialisation : AI & ML"
            }  

            // img.onload = function () { 
            //     console.log('Image loaded successfully'); 
            // } 
            // img.onerror = function () { 
            //     console.error('Error loading image'); 
            //     pp.innerHTML = "Image failed to load. Please check the URL."; 
            //     return; }

            pp.innerHTML = "";
            pp.appendChild(img);
        }