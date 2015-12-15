$(function(){
    // process expert images
    function processExpertImages(){
        var container = $(".expert-image").eq(0);
        var image = $(".expert-image>img");
        var cw = container.width();
        var ch = container.height();
        image.each(function(){
            $(this).css({"border-radius":cw/2});
        });
    };
        
    processExpertImages();
});
