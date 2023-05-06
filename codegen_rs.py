from esdl_construct import *

def ty2rs(type: str) -> str:
    if type == 'int' or type == 'int64':
        return 'i64'
    elif type == 'float' or type == 'float64':
        return 'f64'
    elif type == 'bool':
        return 'bool'
    elif type == 'string':
        assert False, 'string type is special and should not be handled here'
    else:
        return type


def generate_attr_item(attr_item: AttrItem) -> str:
    if len(attr_item.args) == 0:
        return attr_item.ident
    else:
        args = ', '.join([generate_attr_item(arg) for arg in attr_item.args])
        return f'{attr_item.ident}({args})'


def generate_sort(sort: Sort) -> str:
    if len(sort.ctors) == 1:
        return '\n'.join(generate_ctor(sort.ctors[0]))
    else:
        assert False, 'Not implemented yet'


def generate_ctor(ctor: Ctor) -> list[str]:
    doc = ['#[repr(C, u64)]']
    doc.append(f'struct {ctor.name}_Fixed {{')
    for field in ctor.fields:
        if field.optional:
            doc.append(f'    pub has_{field.name}: bool,')
    for field in ctor.fields:
        if not field.repeated and field.ty != 'string':
            doc.append(f'    pub {field.name}: {ty2rs(field.ty)},')
    doc.append('}')
    doc.append('')

    doc.append('#[repr(C, u64)]')
    doc.append(f'struct {ctor.name}_Raw {{')
    doc.append(f'    pub fixed: {ctor.name}_Fixed,')
    for field in ctor.fields:
        if field.repeated:
            if field.ty == 'string':
                doc.append(f'    pub {field.name}: *mut [*const str],')
            else:
                doc.append(f'    pub {field.name}: *mut [{ty2rs(field.ty)}],')
        elif field.ty == 'string':
            doc.append(f'    pub {field.name}: *const str,')
    doc.append('}')
    doc.append('')

    doc.append('#[repr(C, u64)]')
    doc.append(f'struct {ctor.name}_Inplace<\'a> {{')
    doc.append(f'    pub fixed: {ctor.name}_Fixed,')
    for field in ctor.fields:
        if field.repeated:
            if field.ty == 'string':
                doc.append(f'    pub {field.name}: &\'a [&\'a str],')
            else:
                doc.append(f'    pub {field.name}: &\'a [{ty2rs(field.ty)}],')
        elif field.ty == 'string':
            doc.append(f'    pub {field.name}: &\'a str,')
    doc.append('}')
    doc.append('')

    doc.append(f'struct {ctor.name} {{')
    for field in ctor.fields:
        if field.repeated:
            if field.ty == 'string':
                doc.append(f'    pub {field.name}: Vec<String>,')
            else:
                doc.append(f'    pub {field.name}: Vec<{ty2rs(field.ty)}>,')
        elif field.optional:
            doc.append(f'    pub {field.name}: Option<{ty2rs(field.ty)}>,')
        elif field.ty == 'string':
            doc.append(f'    pub {field.name}: String,')
        else:
            doc.append(f'    pub {field.name}: {ty2rs(field.ty)},')
    doc.append('}')
    doc.append('')

    return doc
