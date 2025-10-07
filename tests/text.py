#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Приложение за управление на задачи
Създадено с Python
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class Task:
    """Клас за представяне на задача"""

    def __init__(self, title: str, description: str = "", priority: str = "medium"):
        self.id = self._generate_id()
        self.title = title
        self.description = description
        self.priority = priority  # low, medium, high
        self.completed = False
        self.created_at = datetime.now().isoformat()
        self.completed_at = None

    def _generate_id(self) -> str:
        """Генерира уникален ID за задачата"""
        return str(hash(datetime.now().isoformat()))[-8:]

    def mark_completed(self):
        """Маркира задачата като завършена"""
        self.completed = True
        self.completed_at = datetime.now().isoformat()

    def mark_pending(self):
        """Маркира задачата като незавършена"""
        self.completed = False
        self.completed_at = None

    def to_dict(self) -> Dict:
        """Конвертира задачата в речник"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Създава задача от речник"""
        task = cls(data['title'], data['description'], data['priority'])
        task.id = data['id']
        task.completed = data['completed']
        task.created_at = data['created_at']
        task.completed_at = data['completed_at']
        return task


class TaskManager:
    """Клас за управление на задачи"""

    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks: List[Task] = []
        self.load_tasks()

    def load_tasks(self):
        """Зарежда задачите от файл"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
            except (json.JSONDecodeError, KeyError):
                print("⚠️  Грешка при зареждане на задачите. Започвам с празен списък.")
                self.tasks = []

    def save_tasks(self):
        """Запазва задачите във файл"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([task.to_dict() for task in self.tasks], f,
                          ensure_ascii=False, indent=2)
        except IOError:
            print("⚠️  Грешка при запазване на задачите.")

    def add_task(self, title: str, description: str = "", priority: str = "medium"):
        """Добавя нова задача"""
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Задачата '{title}' е добавена успешно!")

    def list_tasks(self, show_completed: bool = True):
        """Показва всички задачи"""
        if not self.tasks:
            print("📝 Няма задачи в списъка.")
            return

        print("\n" + "=" * 60)
        print("📋 СПИСЪК СЪС ЗАДАЧИ")
        print("=" * 60)

        for i, task in enumerate(self.tasks, 1):
            if not show_completed and task.completed:
                continue

            status = "✅" if task.completed else "⏳"
            priority_icon = {"low": "🟢", "medium": "🟡", "high": "🔴"}[task.priority]

            print(f"\n{i}. {status} {task.title}")
            print(f"   ID: {task.id}")
            print(f"   Приоритет: {priority_icon} {task.priority.upper()}")

            if task.description:
                print(f"   Описание: {task.description}")

            created_date = datetime.fromisoformat(task.created_at).strftime("%d.%m.%Y %H:%M")
            print(f"   Създадена: {created_date}")

            if task.completed and task.completed_at:
                completed_date = datetime.fromisoformat(task.completed_at).strftime("%d.%m.%Y %H:%M")
                print(f"   Завършена: {completed_date}")

    def complete_task(self, task_id: str):
        """Маркира задача като завършена"""
        task = self.find_task(task_id)
        if task:
            task.mark_completed()
            self.save_tasks()
            print(f"✅ Задачата '{task.title}' е маркирана като завършена!")
        else:
            print("❌ Задачата не е намерена.")

    def uncomplete_task(self, task_id: str):
        """Маркира задача като незавършена"""
        task = self.find_task(task_id)
        if task:
            task.mark_pending()
            self.save_tasks()
            print(f"⏳ Задачата '{task.title}' е маркирана като незавършена!")
        else:
            print("❌ Задачата не е намерена.")

    def delete_task(self, task_id: str):
        """Изтрива задача"""
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"🗑️  Задачата '{task.title}' е изтрита!")
        else:
            print("❌ Задачата не е намерена.")

    def find_task(self, task_id: str) -> Optional[Task]:
        """Намира задача по ID"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_statistics(self):
        """Показва статистики за задачите"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        pending = total - completed

        print("\n" + "=" * 40)
        print("📊 СТАТИСТИКИ")
        print("=" * 40)
        print(f"Общо задачи: {total}")
        print(f"Завършени: {completed}")
        print(f"Незавършени: {pending}")

        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"Процент завършени: {completion_rate:.1f}%")


def show_menu():
    """Показва главното меню"""
    print("\n" + "=" * 50)
    print("🎯 УПРАВЛЕНИЕ НА ЗАДАЧИ")
    print("=" * 50)
    print("1. Добави задача")
    print("2. Покажи всички задачи")
    print("3. Покажи само незавършени задачи")
    print("4. Маркирай задача като завършена")
    print("5. Маркирай задача като незавършена")
    print("6. Изтрий задача")
    print("7. Покажи статистики")
    print("8. Изход")
    print("-" * 50)


def main():
    """Главна функция на приложението"""
    print("🎉 Добре дошли в приложението за управление на задачи!")

    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Изберете опция (1-8): ").strip()

        if choice == "1":
            print("\n📝 ДОБАВЯНЕ НА НОВА ЗАДАЧА")
            title = input("Заглавие на задачата: ").strip()
            if not title:
                print("❌ Заглавието не може да бъде празно!")
                continue

            description = input("Описание (опционално): ").strip()

            print("Приоритет:")
            print("1. Нисък (low)")
            print("2. Среден (medium)")
            print("3. Висок (high)")

            priority_choice = input("Изберете приоритет (1-3, по подразбиране 2): ").strip()
            priority_map = {"1": "low", "2": "medium", "3": "high"}
            priority = priority_map.get(priority_choice, "medium")

            manager.add_task(title, description, priority)

        elif choice == "2":
            manager.list_tasks(show_completed=True)

        elif choice == "3":
            manager.list_tasks(show_completed=False)

        elif choice == "4":
            task_id = input("Въведете ID на задачата за завършване: ").strip()
            manager.complete_task(task_id)

        elif choice == "5":
            task_id = input("Въведете ID на задачата за отмяна на завършването: ").strip()
            manager.uncomplete_task(task_id)

        elif choice == "6":
            task_id = input("Въведете ID на задачата за изтриване: ").strip()
            confirm = input("Сигурни ли сте? (да/не): ").strip().lower()
            if confirm in ["да", "yes", "y"]:
                manager.delete_task(task_id)
            else:
                print("❌ Изтриването е отменено.")

        elif choice == "7":
            manager.get_statistics()

        elif choice == "8":
            print("👋 Довиждане! Благодаря, че използвахте приложението!")
            break

        else:
            print("❌ Невалидна опция! Моля, изберете число от 1 до 8.")

        input("\nНатиснете Enter за продължаване...")


if __name__ == "__main__":
    main()