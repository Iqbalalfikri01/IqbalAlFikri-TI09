// menangkap element a dengan menggunakan looping
document.querySelectorAll('#option a').forEach((anchor) => {
    anchor.addEventListener('click', (element) => {
        computerChoice(element);
    })
});

function computerChoice(element){
    // menangkap pilihan user
    let pilihanuser = element.target.innerText;

    // menangkap pilihan komputer pada result
    let pilihankomputer = document.querySelector('#result');

    let hasil = document.querySelector('#hasil');

    // membuat pilihan komputer
    let choices = ['Rock', 'Paper', 'Scissors'];

    // membuat pilihan random untuk komputer
    pilihankomputer.innerHTML = choices[Math.floor(Math.random() * choices.length)];
    pilihankomputer = pilihankomputer.innerHTML;


    // jika user yang menang
    if(pilihanuser == 'Rock' && pilihankomputer == 'Scissors'){
        hasil.innerHTML = 'you win';
    }

    if(pilihanuser == 'Paper' && pilihankomputer == 'Rock'){
        hasil.innerHTML = 'you win';
    }

    if(pilihanuser == 'Scissors' && pilihankomputer == 'Paper'){
        hasil.innerHTML = 'you win';
    }
    
    // jika komputer yang menang
    if(pilihanuser == 'Scissors' && pilihankomputer == 'Rock'){
        hasil.innerHTML = 'you lose';
    }

    if(pilihanuser == 'Rock' && pilihankomputer == 'Paper'){
        hasil.innerHTML = 'you lose';
    }

    if(pilihanuser == 'Paper' && pilihankomputer == 'Scissors'){
        hasil.innerHTML = 'you lose';
    }

    // jika seri atau draw
    if(pilihanuser == pilihankomputer){
        hasil.innerHTML = 'draw';
    }
}