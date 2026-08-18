# Agent Plugins development feedback from August 11 Office Hours

During the August 11, 2026 Python + AI Office Hours, we forked the canonical Agent Plugins example, added the public Microsoft Learn MCP server, and tried to install the resulting plugin in Copilot CLI, VS Code, and ChatGPT.

Test repository: https://github.com/pamelafox/agent-plugins-example

Recording: https://www.youtube.com/watch?v=lYeRqOvohxk

## Reproducible failures

### 1. Copilot CLI reported a successful direct install, but did not install or list the plugin

**Timestamp:** [18:17-20:18](https://www.youtube.com/watch?v=lYeRqOvohxk&t=1097)

**Steps observed:**

1. Follow the documented option to install a plugin from a repository or local path.
2. Run `copilot plugin install owner/repo`.
3. Observe the successful-install message.
4. Run `copilot plugin list` and check the Copilot app's plugin list.

**Observed:** The command said the plugin installed successfully, but the plugin did not appear in `copilot plugin list` or the app's list.

**Expected:** A successful install should make the plugin available and listable. Otherwise, the command should fail with an actionable error.

The CLI also warned that direct plugin installs were deprecated and that a future release would only install plugins from marketplaces. That conflicts with the development workflow described in the documentation.

### 2. The same plugin may have appeared twice after VS Code source installation

**Timestamp:** [20:48-22:17](https://www.youtube.com/watch?v=lYeRqOvohxk&t=1248)

**Steps observed:**

1. Attempt the direct repository install through Copilot CLI; the plugin is not listable.
2. Use VS Code's **Install Plugin from Source** command for the same repository.
3. Open the installed plugins view.

**Observed:** VS Code displayed the plugin twice. One entry may have been residual state from the CLI install and the other from VS Code's source install.

**Expected:** One logical plugin installation should produce one entry, or separate installations should have clearly identified scopes and predictable uninstall behavior.

**Confidence:** Probable issue. The recording shows duplicate entries, but does not establish their internal IDs or installation scopes.

### 3. ChatGPT imported the skill but not the plugin's MCP server

**Timestamps:** [9:27-10:07](https://www.youtube.com/watch?v=lYeRqOvohxk&t=567) and [40:44-40:59](https://www.youtube.com/watch?v=lYeRqOvohxk&t=2444)

**Observed:** A participant first reported that a ChatGPT plugin import made the skill available but not the MCP server. During the session, they tested Pamela's plugin and independently reported the same result: "the plugin you had didn't import the MCP."

**Expected:** Importing a compatible Agent Plugin that contains both a skill and an MCP configuration should import both supported components, or explain why a component was rejected.

This is especially confusing because the compatible-clients page appeared to claim component support. If ChatGPT intentionally does not support this MCP configuration or account type, the compatibility table and import result should say so explicitly.

## Documentation and developer-experience gaps

### 4. There is no clear cross-client workflow for testing a plugin directly from source

**Timestamps:** [16:59-21:05](https://www.youtube.com/watch?v=lYeRqOvohxk&t=1019) and [24:14-29:27](https://www.youtube.com/watch?v=lYeRqOvohxk&t=1454)

VS Code's **Install Plugin from Source** flow worked and installed both the skill and MCP server. The equivalent paths were unclear or broken elsewhere:

* The Copilot app documentation did not make its development-time install path clear.
* Copilot CLI accepted a repository install but warned that direct installs were deprecated, then failed to list the plugin.
* ChatGPT exposed developer mode and plugin creation UI, but the session could not find a straightforward repository import path.
* ChatGPT guidance appeared to require `marketplace.json`, adding marketplace packaging before a developer can test a plugin.

A portable plugin needs one documented local or repository-based smoke-test workflow per compatible client, including prerequisites, account or workspace restrictions, expected UI, validation output, and uninstall/reset steps.

### 5. Repository installs and marketplace-only direction contradict each other

**Timestamp:** [18:17-20:18](https://www.youtube.com/watch?v=lYeRqOvohxk&t=1097)

The workflow said plugins could be installed from a marketplace, repository, or local path. The CLI then warned that direct installs were deprecated and future releases would only support marketplaces.

The team should clarify whether source installs are a permanent development feature, a client-specific feature, or scheduled for removal. If marketplace publication is required for testing, the docs should provide a minimal development marketplace and explain why that extra layer is necessary.

### 6. Copilot app installation instructions were hard to find or missing

**Timestamp:** [16:59-18:17](https://www.youtube.com/watch?v=lYeRqOvohxk&t=1019)

The documentation covered other Copilot surfaces, but the presenter could not find direct instructions for installing into the Copilot app. She eventually inferred that CLI configuration should carry over to the app.

Each supported Copilot client should have its own explicit installation and verification steps. The docs should not require users to infer shared state between CLI, app, and VS Code.

### 7. The canonical example did not exercise the defining skill-plus-MCP scenario

**Timestamp:** [8:05-10:50](https://www.youtube.com/watch?v=lYeRqOvohxk&t=485)

The canonical example was presented as the template to copy, but it did not contain an `mcp.json` example. We had to add one before testing whether a client installed both a skill and an MCP server.

The canonical repository should include a minimal, safe MCP server configuration, automated schema validation, and a smoke test that verifies both components are discovered. A skill-only example does not validate the format's central bundling promise.

### 8. MCP configuration guidance appeared inconsistent

**Timestamp:** [14:04-16:57](https://www.youtube.com/watch?v=lYeRqOvohxk&t=844)

While adding the MCP configuration, different examples or schemas appeared to use different MCP JSON naming or shapes. The presenter initially called it a bug, then wondered whether both forms were supported.

**Confidence:** Documentation ambiguity rather than a confirmed schema defect. The transcript is not clear enough to identify the two exact forms. The team should compare every quickstart, schema, canonical example, and client-specific guide and state which forms are normative versus accepted for compatibility.

## What worked

VS Code's **Install Plugin from Source** flow successfully installed the test plugin. The Microsoft Learn MCP server and the bundled skill both appeared in VS Code with the plugin identified as their source. See [20:48-23:09](https://www.youtube.com/watch?v=lYeRqOvohxk&t=1248).

## Suggested priority

1. Fix or diagnose the Copilot CLI false-success install result.
2. Fix or document ChatGPT dropping the MCP component.
3. Publish a supported source-testing workflow and reconcile it with marketplace-only messaging.
4. Expand the canonical example to include and validate both a skill and an MCP server.
5. Clarify client compatibility, account requirements, installation scope, and MCP configuration variants.

## Scope note

The recording also showed a stale Canvas overlay in the Copilot app at [12:15-12:42](https://www.youtube.com/watch?v=lYeRqOvohxk&t=735). That looked like a Copilot app UI bug, not an Agent Plugins development issue, so it is not included in the findings above.