require.config({
    shim: {
        'input-mask': ['jquery']
    },
    paths: {
        'input-mask': 'assets/plugins/input-mask/js/jquery.mask.min'
    }
});

require(['input-mask', 'jquery'], function(mask, $){
    $(document).ready(function(){
        $.applyDataMask('[data-mask]');
    });
});