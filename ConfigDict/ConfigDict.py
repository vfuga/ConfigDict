#
# 
#
import logging
logger = logging.getLogger("ConfigDict")

class ConfigDict():

    _indent = "  "

    def __init__(self, data=None, default=None):
        if default is not None:
            self._update(default)
        if data is not None:
            self._update(data)

    def _update(self, data):
        if (data is not None) and (isinstance(data, dict) or (isinstance(data, ConfigDict))):
            for k in data:
                if isinstance(data[k],dict):
                    try:
                        _node = self[k]
                        _node._update(data[k])
                    except:
                        _node = ConfigDict(data[k])

                    self.__setitem__(k, _node) 
                else:
                    self.__setitem__(k, data[k])
            return

        if (data is not None):
            raise ValueError("Expect 'dict' or 'ConfigDict' as a parameter")


    def __setitem__(self, key, value):
        _node = self
        keys = key.split('.')
        for k in keys[:-1]:
            if _node.__dict__.get(k) is None:
                _new_node = ConfigDict()
                _node.__setattr__(k, _new_node)
                _node = _new_node
            else:
                _node = _node.__getattribute__(k)

        k = keys[-1]
        _node.__setattr__(k, value)

    def __getitem__(self, key):
        keys = key.split('.')
        _node = self
        for k in keys[:-1]:
            next_node = _node.__dict__.get(k)
            if next_node is None:
                raise AttributeError("'{}' object has no attribute '{}'".format(self.__class__.__name__ , k))
            else:
                _node = next_node

        return _node.__getattribute__(keys[-1])

    @classmethod
    def _adict_repr(cls, o, level:int=0, indent=""):
        _pre = indent*(level+1) if level > 0 else indent
        _img = ""
        if level == 0:
            _img += "{\n"   #1
        _s = ','
        _l = len(o.__dict__)
        if isinstance(o, ConfigDict):
            for e in o.__dict__.items():
                _l -= 1
                if isinstance(e[1], ConfigDict):
                    _img += _pre+'"'+ e[0]+ '":{\n' #2
                    _img += ConfigDict._adict_repr(o=e[1], level=level+1, indent=indent) + "\n"
                else:
                    _img += _pre+'"' + e[0] + '":'+ e[1].__repr__() + _s+"\n"

                if _l == 0:
                    _img = _img[:-2]+"\n"

        if level == 0:
            _img += "}\n"
        else:
            _pre=indent*level if level > 0 else ""
            _img += _pre+'}'+_s
        return _img

    def __repr__(self) -> str:
        return ConfigDict._adict_repr(o=self, level=0, indent=ConfigDict._indent)

    def __str__(self):
        s = ConfigDict._adict_repr(o=self, level=0, indent="")
        return s.replace('\n', '')

    def __len__(self):
        return len(self._getnames(o=self))

    @classmethod
    def _getnames(cls, o, nm:str=''):
        _names = []
        for e in o.__dict__:
            if isinstance(o[e],cls):
                _names.extend(o[e]._getnames(o=o[e], nm=nm+e+'.'))
            else:
                _names.append(nm+e)
        return _names

    def __iter__(self):
        return { e:self[e] for e in self._getnames(self)}.__iter__()
        
    def __call__(self, func, *args, **kvargs):
        logger.info('Run "' + func.__name__ +'"')
        logger.info('Params:' + str(args) + ', ' +str(kvargs))
        func(self, *args, **kvargs)
        return self
       
