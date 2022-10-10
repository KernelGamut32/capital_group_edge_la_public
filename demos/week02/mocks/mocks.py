from unittest.mock import Mock
from unittest.mock import MagicMock
from unittest.mock import ANY
from requests import Session
from unittest.mock import seal

m = Mock(att1='One', att2='Two')
print(m.att1)
print(m.att2)

m = Mock(return_value=42)
print(m())
print(m(18))
print(m('One', 'Two'))

m = Mock(side_effect=range(2))
print(m())
print(m())
# print(m()) # This will throw StopIteration error

m = Mock(side_effect=KeyError)
# m() # This will always throw KeyError
m = Mock(side_effect=['One', 'Two', 'Careful', KeyError])
print(m())
print(m())
print(m())
# print(m()) # This will throw KeyError in series

m = Mock(side_effect=print)
m('One')
m('One', 'Two')


def stub(val):
    return 'Called with {}'.format(val)


m = Mock(side_effect=stub)
print(m('One'))
print(m('Two'))

# fake_name = 'Joe Schmoe'
# payload = {'name': fake_name}

# def get_user_name(user, session):
#     url = f'https://api.github.com/users/{user}'
#     response = session.get(url)
#     json_response = response.json()
#     return json_response['name']

# class FakeSession:
#     def get(self, url):
#         return FakeResponse()

# class FakeResponse:
#     def json(self):
#         return payload

# fake_session = FakeSession()
# assert fake_name == get_user_name('blah', fake_session)

# fake_response = Mock()
# fake_response.json = Mock(return_value=payload)

# fake_session = Mock()
# fake_session.get = Mock(return_value=fake_response)

# assert fake_name == get_user_name('blah', fake_session)

# fake_session = Mock(**{'get.return_value.json.return_value': payload})
# print(fake_session.get())
# print(fake_session.get().json())

# assert fake_name == get_user_name('blah', fake_session)

# fake_session = Mock()
# fake_session.get.return_value.json.return_value = payload
# print(fake_session.get())
# print(fake_session.get().json())

# assert fake_name == get_user_name('blah', fake_session)

# m = Mock()
# mm = MagicMock()

# print(m[0]) # This will not work - requires __getitem__ magic method
# print(m['key1']) # This will not work - requires __getitem__ magic method
# print(m + 1) # This will not work - requires __add__ magic method

# print(mm[0])
# print(mm['key1'])
# print(mm + 1)
# print(mm.prop.method() / 4)

# m = Mock()
# m('One')
# m('Two', 'Three')
# m('One', 'Two', 'Three', kword='Four')

# m.assert_called_with('One', 'Two', 'Three', kword='Four')
# m.assert_called_with('One', 'Two', kword='Four')

# m.assert_any_call('Two', 'Three')
# m.assert_any_call('Two', 'Four')

# m.assert_any_call('One', 'Two', ANY, kword=ANY)

# print(m.called)
# print(m.call_count)

# args, kwargs = m.call_args
# print(args)
# print(kwargs)

# print(m.call_args_list)

# import requests
# session = requests.Session()
# print(get_user_name('KernelGamut32', session))

# spy = Mock(wraps=session)
# print(get_user_name('KernelGamut32', spy))
# print(spy.get)
# print(spy.get.called)
# print(spy.get.call_args)
# spy.get.assert_called_with('https://api.github.com/users/KernelGamut32')

# def get_user_name2(user, session):
#     url = f'https://api.github.com/users/{user}'
#     response = session.get_url(url)
#     json_response = response.json()
#     return json_response['name']

# fake_session = MagicMock()
# fake_session.get.return_value.json.return_value = payload
# print(get_user_name2('KernelGamut32', fake_session))

# fake_session = MagicMock(spec=Session)
# fake_session.get.return_value.json.return_value = payload
# print(get_user_name2('KernelGamut32', fake_session))

# fake_session = MagicMock(spec=Session)
# fake_session.get.return_value.get_json.return_value = payload
# print(get_user_name('KernelGamut32', fake_session))

# fake_session = MagicMock(spec=Session)
# fake_session.get.return_value.get_json.return_value = payload
# seal(fake_session)
# print(get_user_name('KernelGamut32', fake_session))

# m = Mock()
# m.prop1.prop3 = 42
# m.prop2 = Mock(name='not_a_child_mock')
# seal(m)
# m.prop1.new_attribute
# m.prop1.prop3.new_attribute
# m.new_attribute
# m.prop2.new_attribute
# print(m.prop2)
