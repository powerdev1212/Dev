$(function(){
    var pages = $(".summary-sections");
    var sections = $(".pdq-sections");
    var menu = $(".guide-menu");
    var container = $(".guide-menu ul");
    var wrapper = $(".treatment-wr");
    var title = $(".treatment-header");
    
    function setCSS(){
        $(".treatment-header").css({"cursor": "pointer"});
    };
    setCSS();

    function createSectionsMenu(){
        i = 0;
        pages.each(function(){
            $(this).find(".pdq-sections").each(function(){
                var title = $(this).find(".header-title");
                var str = "<li class=\"section-line\"><a ident=\"#" + title.attr('id') + "\">" + title.text() + "</li>";
                $(".guide-menu ul").eq(i).append(str);
            });
            i ++;
        });
    };
    createSectionsMenu();
    
    function hideIfNotOne(){
        if(wrapper.length > 1){
            wrapper.hide();
            menu.hide();
        };
    };
    hideIfNotOne();
    
    $(".section-line").on("click",function(){
        $(this).parent("ul").find(".section-line").removeClass("active");
        $(this).addClass("active");
        var active = $(this).find("a").attr("ident");
        $(".pdq-sections").hide();
        $(active).closest(".pdq-sections").show();
    });
    
    title.click(function(){
        var ident = $(this).attr("ident");
        //hideIfNotOne();
        $(".treatment-wr[ident="+ ident +"]").toggle();
        $(".guide-menu[ident="+ ident +"]").toggle();
    });
});
