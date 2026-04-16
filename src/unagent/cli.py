"""Command-line entrypoint."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from unagent.agent import Unagent
from unagent.config import UnagentConfig


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="unagent",
        description="Not an agent but a friend, coworker, and homie.",
    )
    parser.add_argument("message", nargs="*", help="Message to send to unagent")
    parser.add_argument(
        "--history-size",
        type=int,
        default=None,
        help="Max number of messages kept in memory",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    message = " ".join(args.message).strip()
    if not message:
        parser.print_help()
        return 1

    base_config = UnagentConfig.from_env()
    if args.history_size is None:
        config = base_config
    else:
        config = UnagentConfig(history_size=args.history_size, persona=base_config.persona)

    agent = Unagent(config=config)
    response = agent.respond(message)
    print(response)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
