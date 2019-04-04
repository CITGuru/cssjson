from cssjson import toJSON, toCSS

css = toJSON("example.css", path=True)
# print(css)
# json = toCSS({'rules': {u'.morris-hover.morris-default-style .morris-hover-row-label': {'attr': {u'font-weight': u'bold', u'margin': u'0.25em 0'}}, u'.morris-hover.morris-default-style': {'attr': {u'border-radius': u'10px', u'font-size': u'12px', u'color': u'#666', u'padding': u'6px', u'background': u'rgba(255, 255, 255, 0.8)', u'font-family': u'sans-serif', u'border': u'solid 2px rgba(230, 230, 230, 0.8)', u'text-align': u'center'}}, u'.morris-hover': {'attr': {u'position': u'absolute', u'z-index': u'1000'}}, u'.morris-hover.morris-default-style .morris-hover-point': {'attr': {u'white-space': u'nowrap', u'margin': u'0.1em 0'}}}})
json = toCSS(css)
print(json)
