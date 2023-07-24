from typing import List


class SaveConfig:
    def __init__(self, **kwargs):
        self.save_every: int = kwargs.get('save_every', 1000)
        self.dtype: str = kwargs.get('save_dtype', 'float16')


class LogingConfig:
    def __init__(self, **kwargs):
        self.log_every: int = kwargs.get('log_every', 100)
        self.verbose: bool = kwargs.get('verbose', False)
        self.use_wandb: bool = kwargs.get('use_wandb', False)


class SampleConfig:
    def __init__(self, **kwargs):
        self.sample_every: int = kwargs.get('sample_every', 100)
        self.width: int = kwargs.get('width', 512)
        self.height: int = kwargs.get('height', 512)
        self.prompts: list[str] = kwargs.get('prompts', [])
        self.neg = kwargs.get('neg', False)
        self.seed = kwargs.get('seed', 0)
        self.walk_seed = kwargs.get('walk_seed', False)
        self.guidance_scale = kwargs.get('guidance_scale', 7)
        self.sample_steps = kwargs.get('sample_steps', 20)
        self.network_multiplier = kwargs.get('network_multiplier', 1)


class NetworkConfig:
    def __init__(self, **kwargs):
        self.type: str = kwargs.get('type', 'lierla')
        self.rank: int = kwargs.get('rank', 4)
        self.alpha: float = kwargs.get('alpha', 1.0)


class TrainConfig:
    def __init__(self, **kwargs):
        self.noise_scheduler = kwargs.get('noise_scheduler', 'ddpm')
        self.steps: int = kwargs.get('steps', 1000)
        self.lr = kwargs.get('lr', 1e-6)
        self.optimizer = kwargs.get('optimizer', 'adamw')
        self.lr_scheduler = kwargs.get('lr_scheduler', 'constant')
        self.max_denoising_steps: int = kwargs.get('max_denoising_steps', 50)
        self.batch_size: int = kwargs.get('batch_size', 1)
        self.dtype: str = kwargs.get('dtype', 'fp32')
        self.xformers = kwargs.get('xformers', False)
        self.train_unet = kwargs.get('train_unet', True)
        self.train_text_encoder = kwargs.get('train_text_encoder', True)
        self.noise_offset = kwargs.get('noise_offset', 0.0)
        self.optimizer_params = kwargs.get('optimizer_params', {})


class ModelConfig:
    def __init__(self, **kwargs):
        self.name_or_path: str = kwargs.get('name_or_path', None)
        self.is_v2: bool = kwargs.get('is_v2', False)
        self.is_v_pred: bool = kwargs.get('is_v_pred', False)

        if self.name_or_path is None:
            raise ValueError('name_or_path must be specified')


class SliderTargetConfig:
    def __init__(self, **kwargs):
        self.target_class: str = kwargs.get('target_class', '')
        self.positive: str = kwargs.get('positive', None)
        self.negative: str = kwargs.get('negative', None)
        self.multiplier: float = kwargs.get('multiplier', 1.0)
        self.weight: float = kwargs.get('weight', 1.0)


class SliderConfig:
    def __init__(self, **kwargs):
        targets = kwargs.get('targets', [])
        targets = [SliderTargetConfig(**target) for target in targets]
        self.targets: List[SliderTargetConfig] = targets
        self.resolutions: List[List[int]] = kwargs.get('resolutions', [[512, 512]])