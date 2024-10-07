from typing import Any

from wildlife_tracker.migration_management.migration_path import MigrationPath

class Migration:
    
    def __init__(self, migration_id: int, migration_path: MigrationPath, status: str = "Scheduled") -> None:
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.status = status

    def update_migration_details(self, **kwargs: dict[str, Any]) -> None:
        pass

    def get_migration_details(self) -> dict[str, Any]:
        pass

    def cancel_migration(self) -> None:
        pass