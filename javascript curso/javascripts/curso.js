/*var para = document.querySelector("p");
    para.addEventListener("click", actualizarNombre);

    function actualizarNombre(){
        var nombre = prompt("agrega un nuevo nombre");
        para.textContent = "jugador 1:" + nombre;
    } */

    function crearParafo(){
        var para = document.createElement("p");
        para.textContent = "usted clico en el boton";
        document.body.appendChild(para);
    } 

    var botones = document.querySelectorAll("button");

    for(var i = 0; i < botones.length; i++){
    botones[i].addEventListener("click", crearParafo);
    }
