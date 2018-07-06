from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Help text here ...'

    def add_arguments(self, parser):
        parser.add_argument(
            '-r', '--raise',
            action='store',
            dest='is_raise',
            default=0,
            type=int,
            choices=[0, 1],
            help='Raise exception; 0=no raise, 1=raise',
        )

    def handle(self, *args, **options):
        print('options: ', options)
        if options['is_raise']:
            raise CommandError('test exception')
        self.stdout.write('text')
        self.stdout.write(self.style.ERROR('ERROR'))
        self.stdout.write(self.style.WARNING('WARNING'))
        self.stdout.write(self.style.SUCCESS('SUCCESS'))
        self.stdout.write(self.style.NOTICE('NOTICE'))
