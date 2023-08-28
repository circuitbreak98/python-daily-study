def myxml1(tag, contents="", **attrs):
    if not attrs:
        return f"<{tag}>{contents}</{tag}>"
    else:
        attrs_list = []
        for key, value in attrs.items():
            attrs_list.append(f'{key}="{value}"')
        attrs_string = " ".join(attrs_list)
        return f"<{tag} {attrs_string}>{contents}</{tag}>"

def myxml(tagname, contents="", **kwargs):
    attrs = ''.join([f' {key}="{value}"'
                     for key, value in kwargs.items()])
    return f"<{tagname}{attrs}>{contents}</{tagname}>"


print(myxml('foo'))
print(myxml('foo', 'bar'))
print(myxml('foo', 'bar', a=1, b=2, c=3))