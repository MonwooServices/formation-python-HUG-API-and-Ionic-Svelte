from playhouse.sqliteq import SqliteQueueDatabase

db = SqliteQueueDatabase(
    'buddy-api.db.sqlite',
    use_gevent=False,  # Use the standard library "threading" module.
    autostart=True,  # The worker thread now must be started manually.
    queue_max_size=64,  # Max. # of pending writes that can accumulate.
    results_timeout=5.0)  # Max. time to wait for query to be executed.
