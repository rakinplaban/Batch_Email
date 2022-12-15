document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#openform').addEventListener('click', ()=> {
        document.querySelector('.bg-model').style.display = 'flex';
    });

    document.querySelector('.close').addEventListener('click', ()=> {
        document.querySelector('.bg-model').style.display = 'none';
    });

});