$(function() {
        $(".dragitem").draggable({
            revert: true, revertDuration: 100,
            appendTo : "body",
            start: function() {
              //  $(".dropzone").removeClass('out').addClass('over');
                $(this).addClass('shadow');
            }, 
            stop: function() {
                //$(".dropzone").removeClass('over').addClass('out');
                $(this).removeClass('shadow');
            }
        });
        $(".dropzone").droppable({
            over: function() {
                $(this).removeClass('out').addClass('over');
            },
            out: function(){
                $(this).removeClass('over').addClass('out');
            },
            drop: function(event, ui){
                ui.draggable.appendTo($(this));
                $(this).resize();
                //$(this).children(".trashcontent").appendTo($(ui.draggable));
                $(this).removeClass('over').addClass('out');
                $.getJSON($SCRIPT_ROOT +'_ajax',{
                    a: 'test'
                });
            }

        });
});
