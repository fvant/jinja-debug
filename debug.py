class FilterModule(object):
    '''
    custom jinja2 filter that can be used to output messages to stdout while evaluating templates
    
    The filter does not add anything to the template result, it is invisble.
    '''

    def filters(self):
        return {
            'debug': self.debug,
        }

    def debug(self, text):
      print(text)
      return ''
