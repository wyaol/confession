class CodeVerifyFailException(Exception):
    pass

class BlockTimeException(Exception):

    def __init__(self, rest_block_time, *args, **kwargs):
        super(BlockTimeException, self).__init__(*args, **kwargs)
        self.rest_time = rest_block_time