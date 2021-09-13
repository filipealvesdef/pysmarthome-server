from ariadne import MutationType
from .utils import trigger_action, plugin_to_dict

mutation = MutationType()



@mutation.field('toggle')
def toggle(_, info, id):
    g = info.context['g']
    ctrl = g.plugin_manager.get_controllers()[id]
    return trigger_action(ctrl, 'toggle')


@mutation.field('poweron')
def poweron(_, info, id):
    g = info.context['g']
    ctrl = g.plugin_manager.get_controllers()[id]
    return trigger_action(ctrl, 'on')


@mutation.field('poweroff')
def poweroff(_, info, id):
    g = info.context['g']
    ctrl = g.plugin_manager.get_controllers()[id]
    return trigger_action(ctrl, 'off')


@mutation.field('device_action')
def device_action(_, info, id, action, args=[]):
    g = info.context['g']
    ctrl = g.plugin_manager.get_controllers()[id]
    return trigger_action(ctrl, action, *args)
