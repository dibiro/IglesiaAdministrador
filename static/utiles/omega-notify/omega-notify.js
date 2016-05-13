/*
 *  OmegaNotify - v0.1.0
 *   
 *  http://jqueryboilerplate.com
 *
 *  Made by Erifranck Nuñez
 *  Under MIT License
 */
'use strict';

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ('value' in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError('Cannot call a class as a function'); } }

function OmegaLoading() {
	var defaults = {
		'iconClass': 'fa fa-exclamation-triangle',
		'warning': 'Advertencia desea hacer lo siguiente:',
		'cancelClass': 'boton_secondary_omegasd',
		'confirmClass': 'boton_omegasd',
		'description': '¿Esta Seguro de anular la peticion?',
		'action': function action() {
			console.log("callback undefined");
		},
		'buttonClass': 'btn btn-primary'
	};
	function LoadData(fn) {
		$(fn).append('<div class=o-notify-logo-big><img src="/static/img/Omega.svg" style="width:80%;height:80%"></div>');
	}
	function SaveData() {
		$("body").append("<div class='o-layout-notify'></div>");
		$("body").append("<div class='o-notify-logo'></div>");
	}
	function notify_flipper(message) {
		$('body').append("<div class='o-notify-container'><div class='o-notify-card'><div class='o-notify-flipper'><div class='o-notify-front'><span class='fa fa-check icon_notify'></span></div><div class='o-notify-back'><span class='o-notify-img'></span><div class='o-message'>" + message + "</div></div></div></div></div>");
		$('.o-notify-container').delay(500).show(100, function () {
			$('.icon_notify').animate({
				'font-size': '4em'
			}, 1000, function () {
				$('.o-notify-flipper').delay(1000).addClass('success');
				$('.o-notify-flipper').delay(500).animate({
					right: '150px'

				}, 750);
				$('.o-notify-container').delay(750).fadeOut(2500, function () {
					$('.o-notify-container').remove();
				});
			});
		});
	}
	function notify_basic(message) {

		$('body').append("<div class='o-notify-container'><div class='o-notify-position'><div class='o-notify-target'><span><i class='fa fa-check icon-notify'></i><p style='margin-left:10px;float:right '>" + message + "<p></span></div></div></div>");
		$('.o-notify-container').delay(100).show(100, function () {

			$('.o-notify-target').animate({
				width: '80%'

			}, 500);
			$('span').delay(200).fadeIn(500, function () {
				$('.icon-notify').delay(1000).animate({
					'font-size': '1.6em' }, 1000);
			});
		});
		$('.o-notify-container').delay(3000).fadeOut(1000, function () {
			$(this).remove();
		});
	}
	function notify_success() {
		var message = arguments.length <= 0 || arguments[0] === undefined ? "Guardado Completado" : arguments[0];
		var message2 = arguments.length <= 1 || arguments[1] === undefined ? "guardado exitoso" : arguments[1];

		$('.o-notify-success').remove();
		$('body').append('<div class="o-notify-success"><div class= "o-notify-success-container">' + '<div class="o-notify-success-icon"><i class="fa fa-check"></i>' + '</div><div class="o-notify-success-message"><span>' + message + '<p>' + message2 + '</p></span></div></div>' + '<div class="o-notify-success-footer"><div class="o-notify-success-origin"></div></div></div>');
		$('.o-notify-success').animate({ 'bottom': '0px' }, 1000).delay(2000).animate({ 'bottom': '-50%' }, 500, function () {
			$(this).remove();
		});
	}
	function notify_warning() {
		var message = arguments.length <= 0 || arguments[0] === undefined ? "Advertencia" : arguments[0];
		var message2 = arguments.length <= 1 || arguments[1] === undefined ? "" : arguments[1];

		$('.o-notify-success').remove();
		$('body').append('<div class="o-notify-warning"><div class= "o-notify-warning-container">' + '<div class="o-notify-warning-icon"><i class="fa fa-exclamation-triangle"></i>' + '</div><div class="o-notify-warning-message"><span>' + message + '<p>' + message2 + '</p></span></div></div>' + '<div class="o-notify-warning-footer"><div class="o-notify-warning-origin"></div></div></div>');
		$('.o-notify-warning').animate({ 'bottom': '0px' }, 1000).delay(2000).animate({ 'bottom': '-50%' }, 500, function () {
			$(this).remove();
		});
	}
	function notify_target_up() {
		var message = arguments.length <= 0 || arguments[0] === undefined ? "" : arguments[0];

		$('.o-notify-target').remove();
		$('body').append('<div class="o-notify-target" ><div class="o-notify-target-container" >' + '<div class="o-notify-target-header" ><h6>Guardado Completado</h6></div>' + '<div class="o-notify-target-body" ><p>' + message + '</p></div>' + '<div class="icontarget"><span><i class="fa fa-check"></i></span>' + '</div><div class="o-notify-target-footer"><span><span></div></div></div>');
		$('.o-notify-target').delay(100).animate({ 'height': '200px' }, 500).delay(2000).animate({ 'height': '0px' }, 500, function () {
			$(this).remove();
		}).find('.o-notify-target-footer').children().delay(500).animate({ 'width': '100%' }, 500).parents('.o-notify-target').find('.iconSuccess').children().delay(1000).animate({ 'background-color': 'green', 'font-size': '1.2em' }, 200);
	}
	function notify_basic_fail(message) {

		$('body').append("<div class='o-notify-container'><div class='o-notify-position'><div class='o-notify-target-fail'><span><i class='fa fa-exclamation-triangle icon-notify'></i><p style:'margin-left:10px; float:right'>" + message + "<p></span></div></div></div>");
		$('.o-notify-container').delay(100).show(100, function () {

			$('.o-notify-target-fail').delay(500).animate({
				width: '80%'

			}, 500);
			$('span').delay(800).fadeIn(500, function () {
				$('.icon-notify').delay(1000).animate({
					'font-size': '1.6em' }, 1000);
			});
		});
		$('.o-notify-container').delay(3000).fadeOut(1000, function () {
			$(this).remove();
		});
	}
	function hidden() {
		$('.o-notify-logo').hide(0, function () {
			$('.o-layout-notify').delay(3000).fadeOut(0, function () {
				$(this).remove();
			});
		}).remove();
		$('.o-notify-logo-big').hide().remove();
	}
	function notify_fail() {
		var message = arguments.length <= 0 || arguments[0] === undefined ? "Error al guardar" : arguments[0];
		var message2 = arguments.length <= 1 || arguments[1] === undefined ? "guardado fallido" : arguments[1];

		$('.o-notify-fail').remove();
		$('body').append('<div class="o-notify-fail"><div class= "o-notify-fail-container">' + '<div class="o-notify-fail-icon"><i class="fa fa-exclamation-triangle"></i>' + '</div><div class="o-notify-fail-message"><span>' + message + '<p>' + message2 + '</p></span></div></div>' + '<div class="o-notify-fail-footer"><div class="o-notify-fail-origin"></div></div></div>');
		$('.o-notify-fail').animate({ 'bottom': '0px' }, 500).delay(2000).animate({ 'bottom': '-50%' }, 500, function () {
			$(this).remove();
		});
	}
	function Information(message, iconClass, data) {
		$('body').append("<div class='o-information-container'><div class='o-information-message'>" + "<div class='o-information-message-container'>" + "<div class='o-information-message-header'>" + "<h4><i class='" + iconClass + "'></i>" + message + "</h4></div><div class='o-information-message-body'>" + data + "</div><div class='o-information-message-footer'>" + "</div></div></div></div>");
		$('.o-information-message-container').animate({ 'height': '100%' }, 1000).children().fadeIn(1000).parent().delay(2000).animate({ 'height': '0px' }, 1000).children().delay(2000).fadeOut(2000, function () {
			$(this).parents('.o-information-container').remove();
		});
	}
	function Dialog(options) {
		this.settings = $.extend({}, defaults, options);
		var setting = this.settings;
		$('#OmegaDialog').remove();
		$('body').append('<div class="modal fade" id="OmegaDialog">' + '<div class="modal-dialog"><div class="modal-content"><div class="modal-header">' + '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>' + '<h4 class="modal-title"><i class="' + setting.iconClass + '"></i> ' + setting.warning + 'Desasociar los Solucionadores</h4>' + '</div><div class="modal-body"><h4>' + setting.description + '</h4></div>' + '<div class="modal-footer"><div class="row"><div class="col-sm-5 pull-right">' + '<button type="button" id="CancelAction" class="boton_secondary_omegasd ' + setting.cancelClass + ' " data-dismiss="modal">Cancelar</button>' + '<button type="button" id="ConfirmAction" class="boton_omegasd ' + setting.confirmClass + '">Guardar</button></div></div></div></div></div></div>');
		$('#OmegaDialog').modal({ backdrop: 'static', keyboard: false });
		$('#CancelAction').on('click', function () {
			$('#OmegaDialog').modal('hide');
		});
		$('#ConfirmAction').on('click', function () {
			$('#OmegaDialog').modal('hide');
			setting.action();
		});
	}

	function Alert(options) {
		this.settings = $.extend({}, defaults, options);
		var c = this.settings;
		$('body').prepend("<div class='o-alert'><div class='o-alert-block'><div class='o-alert-block-layout'>" + "</div><div class='o-alert-dialog'>" + "<div class='o-alert-dialog-header'><h3><i class='" + c.iconClass + "'></i>" + c.warning + "</h3></div>" + "<div class='o-alert-dialog-body'>" + c.description + "</div>" + "<div class='o-alert-dialog-footer'><button class='" + c.buttonClass + " o-alert-button'>Aceptar</button>" + "</div></div></div></div>");
		$('.o-alert-dialog').fadeIn(500).delay(300).animate({ 'left': '34%' }, 1).animate({ 'left': '36%' }, 1).animate({ 'left': '35%' }, 1);
		$('.o-alert-button').on('click', function () {
			$('.o-alert-dialog').fadeOut(500, function () {
				$(this).parents('.o-alert').remove();
			});
		});
		$('.o-alert').on('click', function () {
			$('.o-alert-dialog').animate({ 'left': '34%' }, 1).animate({ 'left': '36%' }, 1).animate({ 'left': '35%' }, 1);
		});
	}
	function Confirm(options) {
		this.settings = $.extend({}, defaults, options);
		var setting = this.settings;
		$('.o-confirm').remove();
		$('body').append("<div class='o-confirm'><div class='o-confirm-block'><div class='o-confirm-block-layout'>" + "</div><div class='o-confirm-dialog'>" + "<div class='o-confirm-dialog-body'><i class='" + setting.iconClass + "'></i>" + setting.description + "</div>" + "<div class='o-confirm-dialog-footer'><button class='" + setting.confirmClass + " o-confirm-button' data-boolean='true'>Aceptar</button>" + "<button class='" + setting.cancelClass + " o-confirm-button' data-boolean='false'>Cancelar</button></div></div></div></div>");
		$(".o-confirm-dialog").fadeIn(500);
		confirmation(setting.action, this);
	}
	function confirmation(action, bind) {
		$('.o-confirm-button').on('click', function () {
			if ($(this).data('boolean')) {
				$('.o-confirm-dialog').fadeOut(500, function () {
					$(this).parents('.o-confirm').remove();
					bind.boolean = $(this).data('boolean');
					action();
				});
			} else {
				$('.o-confirm-dialog').fadeOut(500, function () {
					$(this).parents('.o-confirm').remove();
					bind.boolean = $(this).data('boolean');
				});
			}
		});
		return bind.boolean;
	}
	this.saveData = SaveData;
	this.loadData = LoadData;
	this.fail = notify_fail;
	this.warning = notify_warning;
	this.success = notify_success;
	this.flipper = notify_flipper;
	this.hidden = hidden;
	this.information = Information;
	this.alert = Alert;
	this.basic = notify_basic;
	this.dialog = Dialog;
	this.targetInformation = notify_target_up;
	this.boolean = false;
	this.confirm = Confirm;
}
var OmegaNotify = new OmegaLoading();

function compare() {
	return $(".file-drop-zone .file-preview-frame").length * ($(".file-drop-zone .file-preview-frame").width() + 60) > $(".file-drop-zone").width();
}
function resize_upload() {
	return $(".file-drop-zone").css({ 'width': $(".file-drop-zone .file-preview-frame").length * parseInt($(".file-drop-zone .file-preview-frame").css('width')) + parseInt($(".file-drop-zone").css('width')) + 50 + "px" });
}
;(function ($, window, document, undefined) {
	var OmegaPlugin = "OmegaScroll",
	    request = 0,
	    defaults = {
		fade: false
	};

	var Plugin = (function () {
		function Plugin(el, options) {
			_classCallCheck(this, Plugin);

			this.name = OmegaPlugin;
			this.instance = el;
			this.settings = $.extend({}, defaults, options);
			this.rute = 0;
			this.init(el, options);
		}

		_createClass(Plugin, [{
			key: 'init',
			value: function init(el, options) {
				var $conf = this.settings,
				    $wrap = '<div class="carousel-custom"></div>',
				    $left = '<div class="carousel-left"><i class="fa fa-chevron-left fa-2x" ></i></div>',
				    $right = '<div class="carousel-right"><i class="fa fa-chevron-right fa-2x" ></i></div>',
				    $move = $(el),
				    _this = this,
				    $parent = $move.addClass('carousel-move').wrap($wrap).parents('.carousel-custom').append('' + $left + $right);
				$left = $(el).parent().find('.carousel-left');
				$right = $(el).parent().find('.carousel-right');
				$right.on('mousedown', function () {
					requestAnimationFrame(carousel_right);
				});
				$left.on('mousedown', function () {
					requestAnimationFrame(carousel_left);
				});
				function carousel_right() {
					if (_this.rute > -$move.width()) _this.rute -= 20;
					$move.css('transform', 'translateX(' + _this.rute + 'px)');
					request = requestAnimationFrame(carousel_right);
				}
				function carousel_left() {
					if (_this.rute < 0) _this.rute += 20;
					$move.css('transform', 'translateX(' + _this.rute + 'px)');
					request = requestAnimationFrame(carousel_left);
				}
				if ($conf.fade) {
					$move.arrowHidden();
				}
				addEventListener('mouseup', function () {
					cancelRequestAnimFrame(request);
				});
			}
		}]);

		return Plugin;
	})();

	$.fn.omegac = [];
	$.fn[OmegaPlugin] = function (options) {
		var _this2 = this;

		return this.each(function () {
			if (!$.data(_this2, "plugin_" + OmegaPlugin)) {
				$.fn.omegac.push($.data(_this2, "plugin_" + OmegaPlugin, new Plugin(_this2, options)));
			}
		});
	};
	$.fn.arrowHidden = function () {
		$(this).css({ 'margin-left': '0px' }).css('transform', 'translateX(0px)').parent().find('.carousel-left,.carousel-right').hide();
	};
	$.fn.arrowShown = function () {
		$(this).css({ 'margin-left': '25px' }).parent().find('.carousel-left,.carousel-right').fadeIn();
	};
	$('[data-toogle="o-carousel"]').OmegaScroll();
})(jQuery, window, document);

(function ($) {
	var defaults = {
		nclass: 'boton_omegasd',
		pclass: 'boton_secondary_omegasd',
		eclass: 'boton_omegasd',
		endtext: 'importar',
		callbacks: []
	};
	function next($pane, $index, $callback) {
		$($('.wizard-next')[$index]).on('click', function () {
			$($('.wizard-selected')[$index]).addClass('small');
			$($('.wizard-progress')[$index]).addClass('active');
			$($('.wizard-icon')[$index]).addClass('success');
			$pane.addClass('move-right').delay(1500).fadeOut(0, function () {
				if (typeof $callback === "function") $callback();
				$($('.wizard-pane')[$index + 1]).addClass('move-left').fadeIn(0, function () {
					$(this).trigger('shown.wizard');
				}).removeClass('move-left');
				$($('.wizard-selected')[$index + 1]).fadeIn().parent().addClass('active');
			});
		});
	}
	function prev($pane, $index) {
		$($('.wizard-prev')[$index - 1]).on('click', function () {
			$($('.wizard-selected')[$index]).fadeOut().parent().removeClass('active');
			$($('.wizard-progress')[$index - 1]).removeClass('active');
			$pane.addClass('move-left').delay(1500).fadeOut(0, function () {
				$($('.wizard-icon')[$index - 1]).removeClass('success');
				$($('.wizard-selected')[$index - 1]).removeClass('small');
				$($('.wizard-pane')[$index - 1]).addClass('move-right').fadeIn(0, function () {
					$(this).trigger('shown.wizard');
				}).removeClass('move-right');
			});
		});
	}

	var Wizard = (function () {
		function Wizard(el, options) {
			_classCallCheck(this, Wizard);

			this.init(el, options);
		}

		_createClass(Wizard, [{
			key: 'init',
			value: function init(el, options) {
				var $panes = $(el).children('fieldset'),
				    $settings = $.extend({}, defaults, options),
				    $container = $(el),
				    $count = $panes.size(),
				    $parent = '<div class="wizard-container"></div>',
				    $wpanes = '<div class="wizard-header widget box"></div><div class="wizard-body"></div><div class="wizard-footer"></div>',
				    $next = '<button type="button" class="wizard-next ' + $settings.nclass + '">siguiente</button>',
				    $prev = '<button type="button" class="wizard-prev ' + $settings.pclass + '">anterior</button>',
				    $end = '<button type="submit" class="wizard-end ' + $settings.eclass + '">' + $settings.endtext + '</button>',
				    $progress = '<div class="wizard-steps"><div class="wizard-steps-container"></div></div>',
				    $paneStep = '<div class="wizard-step"><i class="wizard-icon fa fa-check"></i><div class="wizard-selected"></div></div>',
				    $paneline = '<div class="wizard-line"><div class="wizard-progress"></div></div>',
				    $callbacks = $settings.callbacks;
				$panes.addClass('wizard-pane').first().before($progress);
				$container.wrapAll($parent);
				$.each($panes, function (index, val) {
					var $step = $(val).children('legend'),
					    $elem = $(val).children();
					$(val).attr('id', 'pane-' + index);
					if (index < $count - 1) {
						if (index === 0) {
							$(val).addClass('active').append($wpanes).find('.wizard-footer').append($next);
							$('.wizard-steps-container').append('' + $paneStep + $paneline);
							$($('.wizard-selected')[index]).parent().addClass('active');
							$elem.appendTo($(val).find('.wizard-body'));
							$step.addClass('widget-header headermodules_style').appendTo($(val).find('.wizard-header'));
							next($(val), index, $callbacks);
						} else {
							$('.wizard-steps-container').append('' + $paneStep + $paneline);
							$(val).append($wpanes).find('.wizard-footer').append('' + $next + $prev).parent().hide();
							$elem.appendTo($(val).find('.wizard-body'));
							$step.addClass('widget-header headermodules_style').appendTo($(val).find('.wizard-header'));
							$($('.wizard-selected')[index]).hide();
							prev($(val), index);
							next($(val), index);
						}
					} else {
						$('.wizard-steps-container').append('' + $paneStep);
						$(val).append($wpanes).find('.wizard-footer').append('' + $end + $prev).parent().hide();
						$elem.appendTo($(val).find('.wizard-body'));
						$step.addClass('widget-header headermodules_style').appendTo($(val).find('.wizard-header'));
						$($('.wizard-selected')[index]).hide();
						prev($(val), index);
					}
				});
			}
		}]);

		return Wizard;
	})();

	$.fn.OmegaWizard = function (options) {
		var _this3 = this;

		return this.each(function () {
			if (!$.data(_this3, "wizard")) {
				$.data(_this3, "wizard", new Wizard(_this3, options));
			}
		});
	};
})(jQuery, document, window);
;(function ($) {
	var OmegaPlugin = "OmegaFile";

	var Plugin = (function () {
		function Plugin(el, options) {
			_classCallCheck(this, Plugin);

			this.settings = $.extend({}, options);
			this.init(el);
		}

		_createClass(Plugin, [{
			key: 'init',
			value: function init(el) {
				var $content = $(el),
				    $parent = '<div class="o-custonboton-upload btn-file min-fileupload" style="margin:0;"> </div>',
				    $icon = '<i class="glyphicon fa fa-upload"></i>',
				    $label = '<div class="o-label-custom">Agregar</div>',
				    $upload = '<div class="name-upload"></div>',
				    $index = 0,
				    $file = '';
				$content.addClass('o-custom-upload').wrap($parent).parent().append('' + $upload + $icon + $label);
				$content.on('change', function () {
					$index = $content.val().lastIndexOf('\\');
					$file = $content.val().substring($index + 1);
					$content.parent().children('.name-upload').text($file);
				});
			}
		}]);

		return Plugin;
	})();

	$.fn[OmegaPlugin] = function (options) {
		var _this4 = this;

		return this.each(function () {
			if (!$.data(_this4, "plugin_" + OmegaPlugin)) {
				$.fn.omegac.push($.data(_this4, "plugin_" + OmegaPlugin, new Plugin(_this4, options)));
			}
		});
	};
})(jQuery, document, window);
window.cancelRequestAnimFrame = (function () {
	return window.cancelAnimationFrame || window.webkitCancelRequestAnimationFrame || window.mozCancelRequestAnimationFrame || window.oCancelRequestAnimationFrame || window.msCancelRequestAnimationFrame || clearTimeout;
})();
window.requestAnimFrame = (function () {
	return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame || function ( /* function */callback, /* DOMElement */element) {
		return window.setTimeout(callback, 1000 / 60);
	};
})();
//# sourceMappingURL=omega-notify.js.map
