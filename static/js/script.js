function cambiar() {
  let siteNav = document.getElementById('nav');
  siteNav.classList.toggle('site-nav-open');
  let bars = document.getElementById('bars');
  bars.classList.toggle('bars-open');
  let times = document.getElementById('times');
  times.classList.toggle('times-open');
}
function validateForm(e){
    var elements = e.elements;
    for(var i = 0; i < elements.length; i++) {
        if(elements[i].tagName === "INPUT" || elements[i].tagName === "SELECT"){
            if(elements[i].value.trim() === "" && elements[i].required === true) {
                var title = elements[i].getAttribute('title');
                alert("Por favor completa el campo " + title);
                elements[i].focus();
                elements[i].style.borderColor = "red";
                elements[i].style.borderStyle = "dashed";
                return false;
            }
        }
    }
}
