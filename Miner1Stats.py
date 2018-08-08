

class Stats():
    '''Stats object to hold list of stats from Miner1's logs.'''
    def __init__(self):
        self.stats = []

    @property
    def stats_list(self):
        return self.stats

    def add_stat(self, new_stat=None):
        '''Append a new stat to the list of stats.'''
        if new_stat is None:
            print('No new stat given, none added.')
        else:
            self.stats.append(new_stat)

    def format_csv(self, unf_stat):
        '''Take a string line and return it split it by ','.'''
        return unf_stat.split(',')  # Mostly for testing purposes.

    def format_claymore_log(self, unf_stat):
        '''Take an unformatted line from a Claymore log and return its items.'''
        # TODO: Parse Claymore log line.
        f_stat = unf_stat
        return f_stat

    def format_stat(self, unf_stat, add_timestamp=False, type='Claymore logs'):
        '''Take an unformatted string and return a list of parsed items.'''

        '''Make a dict of func names to be executed depending on
        the type received. Then, return its result.
        '''
        source_type = {
            'Claymore logs': self.format_claymore_log,
            'csv': self.format_csv
        }
        formatter = source_type.get(type, lambda: 'Invalid type')
        return formatter(unf_stat)



# If Miner1Stats.py is run individually...
if __name__ == '__main__':
    stats = Stats()
    stats.add_stat(stats.format_stat('testing,this,function', type='csv'))
    print(stats.stats_list)
    print(type(stats.stats_list[0]))
    stats.add_stat(stats.format_stat('07:03:53:554	3654	Check and remove old log files...'))
    print(stats.stats_list)
    print(type(stats.stats_list[1]))
