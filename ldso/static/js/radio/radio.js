$(window).load(function(){
var audio;
var playlist;
var tracks;
var current;
var nome1;
var desc1;

init();
function init(){
    current = 0;
    audio = $('audio');
    playlist = $('#playlist');
    tracks = playlist.find('li a');
    len = tracks.length - 1;
    audio[0].volume = .10;
    playlist.find('a').click(function(e){
        e.preventDefault();
        link = $(this);
        current = link.parent().index();
        run(link, audio[0]);
    });
    audio[0].addEventListener('ended',function(e){
        current++;
        if(current == len){
            current = 0;
            link = playlist.find('a')[0];
        }else{
            link = playlist.find('a')[current];    
        }
        run($(link),audio[0]);
    });
}

function run(link, player){
        player.src = link.attr('href');
        nome1 = link.attr('nome');
        desc1 = link.attr('desc');
        document.getElementsByClassName('current')[0].innerHTML = "A tocar: " + nome1;
        document.getElementsByClassName('describe')[0].innerHTML = desc1;
        par = link.parent();
        par.addClass('active').siblings().removeClass('active');
        audio[0].load();
        audio[0].play();
}
});

