from typing import List, Optional

from wildlife_tracker.migration_management.migration import Migration
from wildlife_tracker.migration_management.migration_path import MigrationPath
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationManager:
    
    def __init__(self) -> None:
        self.migrations: dict[int, Migration] = {}
        self.paths: dict[int, MigrationPath] = {}

    def create_migration_path(self, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> MigrationPath:
        pass

    def get_migration_path_by_id(self, path_id: int) -> Optional[MigrationPath]:
        pass

    def get_migration_paths(self) -> List[MigrationPath]:
        pass

    def get_migration_paths_by_species(self, species: str) -> List[MigrationPath]:
        pass

    def get_migration_paths_by_start_location(self, start_location: Habitat) -> List[MigrationPath]:
        pass

    def get_migration_paths_by_destination(self, destination: Habitat) -> List[MigrationPath]:
        pass

    def remove_migration_path(self, path_id: int) -> None:
        pass

    def create_migration(self, migration_path: MigrationPath) -> Migration:
        pass

    def get_migration_by_id(self, migration_id: int) -> Optional[Migration]:
        pass

    def get_migrations(self) -> List[Migration]:
        pass

    def get_migrations_by_status(self, status: str) -> List[Migration]:
        pass
